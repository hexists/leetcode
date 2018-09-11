#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void *a, const void *b) {
        int num1 = *(int *)a;
        int num2 = *(int *)b;

        if( num1 < num2 ) return -1;
        if( num1 > num2 ) return 1;

        return 0;
}

/**
 *  * Note: The returned array must be malloced, assume caller calls free().
 *   */
int* twoSum(int* nums, int numsSize, int target) {
        int i, j, snum, *find = NULL, *org = (int*)malloc(sizeof(int) * numsSize);
        int *rets = (int*)malloc(sizeof(int) * 2);

        memcpy(org, nums, numsSize * sizeof(int));

        qsort(nums, numsSize, sizeof(int), compare);

        for( i = 0, snum = -1; i < numsSize; i++ ) {
                snum = target - nums[i];
                find = bsearch(&snum, nums, numsSize, sizeof(int), compare);
                if(find != NULL && i != (find - nums)) break;
        }

        if(find != NULL) {
                printf("%d, %d\n", target - snum, snum);
                for(i = j = 0, rets[0] = rets[1] = -1; i < numsSize; i++ ){
                        if(target - snum == org[i] || snum == org[i]) rets[j++] = i;

                        if(rets[0] >= 0 && rets[1] >= 0) break;
                }
                printf("[%d, %d]\n", rets[0], rets[1]);
                return rets;
        }

        return NULL;
}

int main()
{
        // int nums[4] = {7, 2, 11, 15};
        //      // int target = 9;
        // int nums[4] = {-3, 4, 3, 90};
        // int target = 0;
        int nums[5] = {-1, -2, -3, -4, -5};
        int target = -8;

        twoSum(nums, 5, target);

        return 0;
}
