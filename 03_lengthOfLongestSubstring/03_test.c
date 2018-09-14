#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

int lengthOfLongestSubstring(char* s) {
	int repeat[26] = {0, };
	int i, len, max;
	char *prev = NULL, *curr = s;

	printf("%s\n", s);

	while(curr != NULL) {
		if(prev == NULL || *prev != *curr && repeat[*curr]) {
			repeat[*curr]++;
			len++;
		}
		else {
			if(max < len) max = len;
			len = 1;
			// init repeat
			memset(repeat, 0, sizeof(int) * 26);
		}

		prev = curr;

		curr++;
	}
}

int main() {
	// test_case1
	char *str = "abcabcbb";

	lengthOfLongestSubstring(str);

	return 0;
}
