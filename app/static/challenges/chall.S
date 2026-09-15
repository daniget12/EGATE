main:
    mov r0, #4134207980
    mov r1, #950176538
    cmp r0, r1
    bgt print_r0
    print_r1:
        // prints r1 in hex
        bx lr
    print_r0:
        // prints r0 in hex
        bx lr
