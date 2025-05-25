.model small
.stack 100h


.data
    buffer db 256        ; buffer to store the input string
    prompt db "Enter a string: $"
    prompt_len equ $-prompt
    crlf db 0dh, 0ah, "$" ; carriage return and line feed for printing

.code
    mov ax, @data        ; initialize data segment
    mov ds, ax

    lea dx, prompt       ; print prompt message
    mov ah, 09h
    int 21h

    mov ah, 0ah           ; read string from keyboard
    mov dx, offset buffer
    int 21h

    lea si, buffer        ; load address of input buffer into SI
    lea di, buffer        ; load address of output buffer into DI
    xor cx, cx            ; clear CX register

    convert_loop:
        lodsb             ; load next character from input buffer
        cmp al, 0dh       ; check if it's a carriage return
        je done           ; if it is, jump to done

        mov bl, al        ; move character to BL register
        mov bh, 0         ; clear BH register
        mov ax, 0         ; clear AX register
        mov cl, 4         ; shift 4 bits at a time
        shl bl, cl        ; shift left by 4 bits
        or ax, bx         ; combine into ASCII code
        shl ax, cl        ; shift left by 4 bits
        or ax, bx         ; combine into ASCII code
        stosw             ; store ASCII code in output buffer
        inc cx            ; increment CX register

        jmp convert_loop  ; loop back to process next character

    done:
        lea dx, crlf      ; print new line
        mov ah, 09h
        int 21h

        mov ah, 4ch       ; exit program
        int 21h

end


