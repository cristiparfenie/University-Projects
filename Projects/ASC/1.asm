bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit,printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import printf msvcrt.dll                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
;Se dau doua siruri de octeti S1 si S2. Sa se construiasca sirul D prin concatenarea
; elementelor din sirul S1 1uate de la stanga spre dreapta si a elementelor din sirul S2 luate de la 
;dreapta spre stanga. 
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    sir1 db 1,2,3,4
    l1 equ $-sir1
    sir2 db 5,6,7
    l2 equ $-sir2
    d times (l1+l2) db 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ecx,l1
        jecxz sfarsit
        mov esi,0
        loop1:
            mov eax, [sir1+esi]
            mov [d+esi], eax 
            inc esi 
            
        loop loop1
        mov ecx,l2 
        jecxz sfarsit
        
        
        mov ebx, esi
        mov esi, l2
        loop2:
            mov eax, [sir2+esi-1]
            mov [d+ebx], eax 
            inc ebx
            dec esi
        loop loop2
     
          
        
       sfarsit:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
