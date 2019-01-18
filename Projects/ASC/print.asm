%ifndef modul
%define modul
extern printf
import printf  msvcrt.dll

segment data2 use32 class=data
    format db "%o,%c",0

module:
pop ebx
push format
call [printf]
add esp,4*2
push ebx
ret



%endif