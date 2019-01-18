#Binomial(n,p)
p = input("p=");
n = input ("n=");
f=0;
for i = 1 : 1000
  x = 0;
  for j= 1:n
  a=rand();
  if a>p
    #disp(0);
    f=1;
  else 
    #disp(f);
   f=0;   
  endif
  x = x + f;
endfor
disp(x);
endfor
