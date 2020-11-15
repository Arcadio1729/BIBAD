import string
latin_variables=string.ascii_lowercase
constants="01"
operators="|&~()"

def check_sequence(sequence):
    sequence=sequence.replace(" ","")
    current_state="variable_state"
    counter=0
    for s in sequence:
        if current_state=="variable_state":
            if s in latin_variables or s in constants:
                current_state="operator_state"
                continue
            if s=="~":
                current_state="variable_state"
                continue
            if s=="(":
                current_state="variable_state"
                counter+=1
                continue
            return False
        else:
            if s=="|" or s=="&":
                current_state="variable_state"
                continue
            if s==")" and counter>0:
                counter-=1
                continue
            return False
    if counter==0 and current_state!="variable_state":
        return True
    else:
        return False


if __name__ == "__main__":
    true_sequences_test = ["a", "a|b", "a & b | a", "(a &b) |c&~d", "~~a", "~(a|c)", "(a)"]
    false_sequences_test = ["~", "a|", "A|B", "a|&b", "b~", "(a|b", "a|b)"]

    for t in true_sequences_test:
        print(check_sequence(t))

    for f in false_sequences_test:
        print(check_sequence(f))