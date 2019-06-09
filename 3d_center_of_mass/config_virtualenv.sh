#!/bin/bash

if [ "$1" == "--help" ]; then
	echo -e "USAGE:\n$0 [env_name]\n"
else
	if [ -f "/usr/local/bin/virtualenvwrapper.sh" ]; then
		source /usr/local/bin/virtualenvwrapper.sh
	else
		source ~/.local/bin/virtualenvwrapper.sh
	fi

	folder_name=${PWD##*/}
	if [ ! -z $1 ]; then
		env_name=$1
	else
		echo "Using default name ${folder_name}"
		env_name=${folder_name}
	fi

	if [ -f "dev-requirements.txt" ]; then
		requirements="-r dev-requirements.txt"
	elif [ -f "dev-requirements.txt" ]; then
		requirements="-r requirements.txt"
	else
		requirements=""
	fi
	cd .. && \
		mkvirtualenv -p python3 -a ${folder_name} ${requirements} ${env_name} && \
		echo -e "\n\n\nRUN 'workon ${env_name}'\n"
		exit 0 || \
	echo "Need virtualenv and virtualenvwrapper installed." && exit 1;
fi
