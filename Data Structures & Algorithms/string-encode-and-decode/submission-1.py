class Solution:

    def encode(self, strs: List[str]) -> str:
        # We need to essentially "encrypt" the message and ensure it does not coincide with any strings in the list

        # The trick here is to include the length of the word to iterate through the set of characters
        # We always attach the length of the string infront of the string, as well as another character to determine the end of the number, so that when decoding, we will know how many characters to iterate
        encoded_str = []
        for s in strs:
            length = len(s)
            encoded_str.append(str(length) + "#" + s)
        # print(encoded_str)
        return "".join(encoded_str)


    def decode(self, s: str) -> List[str]:
        # When decoding, we first grab the number of characters we are reading from, then attach it to the final result
        # print("encoded string is", s)
        res = []
        i = 0

        while i < len(s):
            str_digit = ""
            # Retrieve the digit length first
            while s[i] != "#":
                str_digit += s[i]
                i += 1
            i += 1 # Shift the pointer to the actual starting letter of the word
            int_digit = int(str_digit) # Convert it to the actual length
            # print("length of actual string", int_digit)
           
            decoded_str = s[i : i + int_digit]
            # print(decoded_str)
            res.append(decoded_str)
            i = i + int_digit
        return res
