bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    s1 db '1','2','3','4','5','6','7','8','9',0
    len1 equ $-s1 
    s2 db 'm','n','0',0
    len2 equ $-s2
    dest times (len1+len2) db 0
    
;Se dau doua siruri de caractere S1 si S2. 
;Sa se construiasca sirul D prin concatenarea elementelor de pe
;pozitiile multiplu de 3 din sirul S1 cu elementele sirului S2 in ordine inversa. 
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ecx,len1 
        mov esi,0
        mov ebx,0
        mov edx,0
        jecxz sir2
        loop1:
              
              mov eax,esi  
              test eax, 0x00000003 
              je convine
              jmp sf
              convine:
                     mov dl,[s1+esi]
                     mov [dest+ebx],al
                     inc ebx
              sf:
              inc esi
       loop loop1
       sir2:
       mov esi,len2
       mov ecx,len2 
       jecxz final
       loop2:
              mov al,[s2+esi-1]
              mov [dest+ebx],al
              mov dl,al
              dec esi 
       loop loop2
       
       final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
