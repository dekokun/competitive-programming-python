TESTINT_TOOL_NAME := testing_tool.py
TESTINT_TOOL_PATH := https://codejam.googleapis.com/dashboard/get_file/AQj_6U3hs6l9rQazzRbH77KTAj6MDmV_lNWQYxNLANPV16oNwtQbyxWzfj9LruA64ETFqg/testing_tool.py
TEST_NUM := 1

interactive_runner.py:
	wget https://storage.googleapis.com/coding-competitions.appspot.com/interactive_runner.py

$(TESTINT_TOOL_NAME):
	wget $(TESTINT_TOOL_PATH)

.PHONY: test
test: interactive_runner.py $(TESTINT_TOOL_NAME) main.py
	python3 interactive_runner.py python3 $(TESTINT_TOOL_NAME) $(TEST_NUM) -- python3 main.py
