#!/bin/bash

if [ "$1" -eq "--help" ]; then
	echo -e "USAGE:\n$0 [env_name]\n"
fi

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

cd .. && \
	mkvirtualenv -p python3 -a ${folder_name} -r dev-requirements.txt ${env_name} && \
	echo -e "\n\n\nRUN 'workon ${env_name}'\n"
	exit 0 || \
echo "Need virtualenv and virtualenvwrapper installed." && exit 1;
