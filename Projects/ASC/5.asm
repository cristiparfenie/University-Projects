bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
;Se dau doua siruri de octeti S1 si S2 de aceeasi lungime. 
;Sa se obtina sirul D prin intercalarea elementelor celor doua siruri. 
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    s1 db 1,2,3,4
    s2 db 5,6,7,8 
    len equ $-s1 
    dest times len db 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ecx,len
        jecxz final
        mov ebx,0
        mov edx,0
        mov esi,0
        loop1:
            test esi, 0x00000001
            jpo ss2
            mov al,[s1+ebx]
            mov [dest+esi],al 
            inc ebx
            jmp sf
            ss2:
            mov al,[s2+edx]
            mov [dest+esi],al
            inc edx
            sf:
            inc esi 
       loop loop1
        
        final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
