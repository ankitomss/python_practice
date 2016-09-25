def remove_substr(s, sub):
    i=s.find(sub)
    if i== -1:
        return s
    s=s[:i]+s[i+len(sub):]
    return remove_substr(s,sub)

s="ankit verms is my name an sdsh aann"

sub="an"
print remove_substr(s,sub)

print s.strip(sub)
print s.replace("an", "")