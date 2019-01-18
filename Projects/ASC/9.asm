bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
;Se da un sir de octeti S. Sa se construiasca un sir D1 
;care sa contina toate numerele pozitive si un sir D2 care sa contina toate numerele negative din S. 
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    s db -1,2,3,4,-2,-7,7
    len equ $-s
    dn times len db 0
    dp times len db 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ecx,len
        jecxz final
        mov ebx,0
        mov esi,0
        mov edx,0
        loop1:
            mov al,[s+esi]
            cmp al,0
            jl below
            mov [dp+edx],al
            inc edx 
            jmp sf
            below:
                mov [dn+ebx],al
                inc ebx
                mov ah,al 
            sf:
            inc esi 
            
        loop loop1
        final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
