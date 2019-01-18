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
    sir db 1,2,3,4,5,6,7,8,9,0,11,12,23,44
    len equ $-sir
    ma db 0
    mi db 1000
;Se da un sir de octeti S. 
;Sa se determine maximul elementelor de pe pozitiile pare si minimul elementelor de pe pozitiile impare din S. 
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ecx,len 
        jecxz final
        mov esi,0
        loop1:
            mov al,[sir+esi]
            test esi,0x00000001
            jpe par
            mov bl,[mi]
            cmp al,bl
            jb maimic
            jmp fin 
            maimic:
                mov [mi],al
                mov dl,al
            par:
                
                mov bl,[ma]
                cmp al,bl
                jg maimare
                jmp fin
                maimare:
                    mov [ma],al
                    mov dh,al
            fin:
            inc esi 
        loop loop1
        
        final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
