make:
	echo "making"
test:
	chmod -R 777 ./answer
	chmod -R 777 ./script_test
	gcc ./answer/fork.c -o ./fork
	gcc ./answer/psh1.c -o ./psh1
	gcc ./answer/psh2.c -o ./psh2

	bash ./script_test/test0.sh
	bash ./script_test/test1.sh
	bash ./script_test/test2.sh



done:
	#rm -rf ./tests/pc_pid_out
	#rm -rf ./tests/mmyfork_out
	echo "delete all"

