bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

%include "print.asm"

; declare external functions needed by our program
extern exit,printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import printf  msvcrt.dll                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    min db 32
    max db 126
    
    
; our code starts here
segment code use32 class=code
    start:
        mov ecx,0
        mov ecx, [min]
        loopp:
        push ecx
        call module
        inc ecx
        cmp ecx,[max]
        jbe loopp
        
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
