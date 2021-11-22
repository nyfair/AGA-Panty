# coe key hack
```
83 e9 04                  sub ecx, 4
83 e1 7f                  and ecx, 7Fh
3b c8                     cmp ecx, eax
74 [1C]                   jz short ??           <- 随机事件暗桩，改成jmp(74->eb)，旧版长jmp需补一位00(例0f84 dd03->e9 de03[偏移量+1] 00)
                          lea rcx, aAgtFluff;   "AGT fluff\n"
                          call xxxx
```
```
41 83 e0 7f               and r15d, 7Fh
45 3b c1                  cmp r15d, r8d
74 [20]                   jz short ??           <- 回合结算暗桩，改成jmp(74->eb)，两暗桩后面call的函数是同一个
                          lea rcx, aBarbQqq32;  "barb qqq 32\n"
                          call xxxx
```
```
83 3d [d6 27 1b 06] 00    cmp cs:dword_????, 0
75 [34]                   jnz short ??          <- CD key校验，改成jmp(75->eb)
b9 05                     mov ecx, 5
若干行之后           lea rcx, aYourCdKeyIsInv;   "Your CD key is invalid"
```
```
                    lea rcx, aMain;             "main"
e8 [d7 62 fc ff]    call sub_??
48 8d 4c 24 [58]    lea rcx, [rsp+?]
e8 [9d 71 04 00]    call sub_??                 <- 启动自检，改成mov eax,1之后补00(b8 01 00 00 00)
85 c0               test eax, eax
```
```
0f bf c8      movsx ecx, ax
85 c9         test ecx, ecx
7f [24]       jg short ??                       <- 联机key检测，改成jmp(7f->eb)
              lea rcx, aKeyAuthenticat;         "Key authentication failed (%d). Make sure no one else is using the same serial key."
```
