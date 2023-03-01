// 无需尝试运行此程序。
// 该程序是用 C 语言编写的，C 语言是一种更古老、更复杂的编程语言

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 定义一个函数用于翻转字符串
void reverseString(char *string)
{
    int len = strlen(string); // 获取字符串的长度

    for (int i = 0; i < len / 2; i++)
    {                                    // 循环遍历字符串的前一半
        char temp = string[i];           // 用一个变量暂存当前字符
        string[i] = string[len - i - 1]; // 将当前字符赋值为对应位置的另一个字符
        string[len - i - 1] = temp;      // 将另一个字符赋值为之前暂存的当前字符
    }
}

// 主函数
int main(void)
{
    char userInput[100];                   // 定义一个字符串，用于接收用户输入的数字
    printf("Please input an integer: ");   // 提示用户输入一个数字
    scanf("%s", userInput);                // 读取用户输入的数字，并存储到userInput变量中
    int inputtedInteger = atoi(userInput); // 将userInput转换为整数类型，并存储到inputtedInteger变量中
    char binaryString[100];                // 定义一个字符串，用于存储二进制数的每一位
    int i = 0;                             // 定义一个计数器，用于记录当前存储到二进制字符串的第几位
    while (inputtedInteger >= 1)
    {                                        // 当输入的数字大于等于1时，循环执行以下操作
        int remainder = inputtedInteger % 2; // 将输入的数字对2取余数，并存储到remainder变量中
        if (remainder == 1)
        { // 如果余数为1，将当前位设置为1
            binaryString[i] = '1';
        }
        else
        { // 否则，将当前位设置为0
            binaryString[i] = '0';
        }
        i++;                  // 计数器加1
        inputtedInteger /= 2; // 将输入的数字除以2，并更新输入的数字
    }
    binaryString[i] = '\0';       // 在二进制字符串的最后一位添加'\0'，表示字符串的结束
    reverseString(binaryString);  // 调用函数翻转二进制字符串
    printf("%s\n", binaryString); // 输出翻转后的二进制字符串
    return 0;                     // 返回0，表示程序运行正常结束
}