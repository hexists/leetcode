#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

int lengthOfLongestSubstring(char* s) {
	char repeat[256] = {0, };
	int i, len = 0, max = 0, n = strlen(s);
	char *prev, *curr;

	for(i = 0; i < n; i++) {
		prev = NULL;
		curr = &s[i];
		len = 0;
		memset(repeat, 0, sizeof(char) * 256);

		if(n - i <= max) break;

		while(*curr != '\0') {
			// if(prev != NULL) printf("%c %c\n", *prev, *curr);

			if(prev == NULL) {
				repeat[*curr] = 1;
				len++;
			}
			else if (*prev != *curr && repeat[*curr] == 0) {
				repeat[*curr] = 1;
				len++;
			}
			else {
				if(max < len) max = len;
				// init repeat
				memset(repeat, 0, sizeof(char) * 256);
				// set curr
				len = 1;
				repeat[*curr] = 1;
			}
			prev = curr;

			// printf("len : %d, max : %d\n", len, max);

			curr++;
		}

		if(max < len) max = len;
		
		// printf("max : %d, %s\n", max, &s[i]);
	}

	// printf("final max : %d\n", max);

	return max;
}

int main() {
	// test_case1 : abc, 3
	// char *str = "abcabcbb";
	// test_case2 : b, 1
	// char *str = "bbbbb";
	// test_case3 : wke, 3
	// char *str = "pwwkew";
	// test_case3 :  , 1
	// char *str = " ";
	// test_case4 : ab, 2
	// char *str = "aab";
	// test_case5 : vdf, 3
	// char *str = "dvdf";
	// test_case6 : sjrgap, 6
	char *str = "asjrgapa";

	int num = lengthOfLongestSubstring(str);

	printf("%d\n", num);

	return 0;
}
