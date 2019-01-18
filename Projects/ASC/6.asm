bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
;Se da un sir de octeti S. 
;Sa se obtina sirul D1 ce contine toate numerele pare din S si sirul D2 ce contine toate numerele impare din S. 
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    sir db 1,2,3,4,5,6,4,5
    len equ $-sir 
    d1 times len db 0
    d2 times len db 0
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ecx, len 
        jecxz final
        mov esi,0
        mov ebx,0
        mov edx,0
        loop1:
            mov al,[sir+esi]
            test al,0x00000001
            jpe par
            mov [d2+edx],al
            mov ah,al
            inc edx
            jmp sf
            par:
                mov [d1+ebx],al
                
                inc bx
            sf:
            inc esi 
       loop loop1
        
        final:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
