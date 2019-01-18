bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
;Se dau 2 siruri de octeti S1 si S2 de aceeasi lungime. 
;Sa se construiasca sirul D astfel incat fiecare element din D sa reprezinte
;maximul dintre elementele de pe pozitiile corespunzatoare din S1 si S2. 
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    s1 db 1,5,3,7,8
    len equ $-s1 
    s2 db 2,4,6,5,9
    dest times len db 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        mov ecx,len 
        jecxz sfarsit
        mov esi,0
        loop1:
            mov al,[s1+esi]
            mov bl,[s2+esi]
            cmp al,bl
            ja mare
            mov [dest+esi],bl
            mov dh,bl
            jmp sf
            mare:
                mov [dest+esi],al
                mov dl,al
            sf:
            inc esi
         loop loop1
         sfarsit:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
