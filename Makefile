APP_SRC_ROOT=test-src

test1:
	gcc  $(APP_SRC_ROOT)/test1.c -Iinclude/ include/*.c -o ./bin/test1 

test2:
	gcc  $(APP_SRC_ROOT)/test2.c -Iinclude/ include/*.c -o ./bin/test2