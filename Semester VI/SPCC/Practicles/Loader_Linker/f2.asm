.model small
.stack 100h

.data
message db 13,10,"Hello World!$"

.code
WinMain proc near
   lea dx, message
   mov ah, 09h
   int 21h

   mov ah,4ch
   int 21h
end WinMain