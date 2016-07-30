#!/usr/bin/python


g = 5 #Primitive root
p = 23 #Prime number

AliceSecret = 15655 #random number by alice
BobSecret = 9666  #random number by bob

AliceA = g ** AliceSecret % p #generate the unique value for Alice
BobA   = g ** BobSecret   % p #generate the unique value for Bob

AliceSharedSecret = BobA ** AliceSecret % p #calculate the shared secret based on AliceA
BobSharedSecret   = AliceA ** BobSecret % p #calculate the shared secret based on BobA

print "Alice Secret is : %s"%AliceSecret
print "Bob   Secret is : %s"%BobSecret
print "*" * 25
print "Alice unique value is %s"%AliceA
print "Bob   unique value is %s"%BobA
print "*" * 25
print "The Final Secret Key For Alice is : %s"%AliceSharedSecret
print "The Final Secret Key for Bob   is : %s"%BobSharedSecret


