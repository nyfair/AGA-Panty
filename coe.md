# coe key hack
```
83 e9 04         sub ecx, 4
83 e1 7f         and ecx, 7Fh
3b c8            cmp ecx, eax
0f 84 [?? ??]    jz ????               <- 随机事件暗桩，改成jmp补一位00(例0f84 dd03->e9 de03[偏移量+1] 00)
                 lea rcx, aAgtFluff  ; "AGT fluff\n"
                 call xxxx
```
```
41 83 e7 7f      and r15d, 7Fh
45 3b f8         cmp r15d, r8d
74 [20]          jz short ??           <- 回合结算暗桩，改成jmp(74->eb)，两暗桩后面call的函数是同一个
                 lea rcx, aBarbQqq32 ; "barb qqq 32\n"
                 call xxxx
```
```
83 [3d d6 27 1b 06 00]    cmp cs:dword_????, 0
75 [34]                   jnz short ?? <- CD key校验，改成jmp(75->eb)
b9 05                     mov ecx, 5
若干行之后
                          lea rcx, aYourCdKeyIsInv ; "Your CD key is invalid"
```
```
                    lea rcx, aMain           ; "main"
e8 [d7 62 fc ff]    call sub_??
[48 8d 4c 24 58]    lea rcx, [rsp+XX+YY]
e8 [9d 71 04 00]    call sub_?? <- 启动自检，改成mov eax,1之后补00(b8 01 00 00 00)
85 c0               test eax, eax
```
```
41 3b fc            cmp edi, r12d
75 [04]             jnz short ?? <- 黑key检测，改成jmp(75-eb)
8b c5               mov eax, ebp
```
