if __name__=="__main__":
    T=int(input())
    name_list=[]
    for i in range(T):
        input_name=input().split()
        name_list.append(input_name)
    for single_name in range(len(name_list)):
        for single_word in range(len(name_list[single_name])):
            name_list[single_name][single_word] = name_list[single_name][single_word].title()
    for name in name_list:
        print(*name)
        