#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// https://leetcode.com/problems/add-two-numbers/

// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

void printListNode(struct ListNode* node) {
	struct ListNode *nodePtr = node;
	while(nodePtr != NULL) {
		printf("%d => ", nodePtr->val);
		nodePtr = nodePtr->next;
	}
	printf("\n");
}

struct ListNode* newNode(int val) {
	struct ListNode *node = (struct ListNode*)malloc(sizeof(struct ListNode));
	node->val = val;
	node->next = NULL;
	return node;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
	printListNode(l1);
	printListNode(l2);

	struct ListNode *aPtr = l1;
	struct ListNode *bPtr = l2;
	struct ListNode *newList = newNode(0), *nPtr = newList;
	int sum = 0, val = 0, isStart = 0;

	while(aPtr != NULL || bPtr != NULL) {
		if(sum >= 10) sum = 1;
		else          sum = 0;
		if(aPtr != NULL) sum += aPtr->val;
		if(bPtr != NULL) sum += bPtr->val;
		val = sum % 10;
		
		if(isStart == 0) {
			nPtr->val = val;
			isStart = 1;
		}
		else {
			nPtr->next = newNode(val);
			nPtr = nPtr->next;
		}

		if(aPtr) aPtr = aPtr->next;
		if(bPtr) bPtr = bPtr->next;
	}

	if(sum >= 10) {
		nPtr->next = newNode(1);
	}

	printListNode(newList);

	return newList;
}

int main() {

	// test case1
	// struct ListNode *alist = newNode(2);
	// struct ListNode *alist2 = newNode(4);
	// struct ListNode *alist3 = newNode(3);

	// struct ListNode *blist = newNode(5);
	// struct ListNode *blist2 = newNode(6);
	// struct ListNode *blist3 = newNode(4);

	// alist->next = alist2;
	// alist2->next = alist3;

	// blist->next = blist2;
	// blist2->next = blist3;

	// test case2
	// struct ListNode *alist = newNode(1);
	// alist->next = newNode(8);

	// struct ListNode *blist = newNode(0);

	// test case3
	struct ListNode *alist = newNode(5);
	struct ListNode *blist = newNode(5);

	addTwoNumbers(alist, blist);

	free(alist);
	free(blist);

	return 0;
}
