bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
;Se dau doua siruri de octeti S1 si S2 de aceeasi lungime. Sa se construiasca sirul D astfel:
;fiecare element de pe pozitiile pare din D este suma elementelor de pe pozitiile corespunzatoare din S1 si S2, 
;iar fiecare element de pe pozitiile impare are ca si valoare diferenta elementelor de pe
;pozitiile corespunzatoare din S1 si S2. 
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    sir1 db 1,2,3,4
    len equ $-sir1 
    sir2 db 6,7,8,9
    dest times len db 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ecx,len
        jecxz sfarsit
        mov esi,0
        loop1:
            mov al,[sir1+esi]
            mov bl,[sir2+esi]
            test esi, 0x00000001 
            jp par
            sub al,bl
            mov [dest+esi],al
            jmp fin
            par:
                add al,bl
                mov [dest+esi],al
            fin:
            inc esi
        loop loop1
        
        sfarsit:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
