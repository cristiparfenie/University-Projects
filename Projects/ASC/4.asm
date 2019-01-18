bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
;Se da un sir de octeti S de lungime l. Sa se construiasca sirul D de lungime l-1 
;astfel incat elementele din D sa reprezinte diferenta dintre fiecare 2 elemente consecutive din S. 
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    src db 1,2,3,4,5,6,7,8
    len equ $-src 
    dest times len db 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ecx, len
        dec ecx
        jecxz sfarsit
        mov esi,0
        loop1:
            mov al,[src+esi]
            mov bl,[src+esi+1]
            sub bl,al 
            mov [dest+esi],bl
            inc esi 
        loop loop1
        
        sfarsit:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
