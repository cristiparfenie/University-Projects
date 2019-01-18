disp("Hello World");

a=input("a: ")
f=0;
for i = 1 : 1000
    b=rand()
    if b>a
        disp(0)
        f=f+1;
else
    disp(f);
    f=0;
endif
endfor