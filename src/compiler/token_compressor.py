""" The file where the definition of the TokenCompressor
class is stored. """

from tokenizer import Tokenizer


class TokenCompressor:
    """ The class the compresses tokens into
    a format the compiler can understand for bytecode
    conversion and post-compilation interpretation. """
    
    def __init__(self, tokenizer_obj: Tokenizer, compress_id: int):
        """ Initializes the class and handles
        init-vars. @member token_list is the passed
        list to compress. """
        self.tokens = []
        self.compress_id = int(compress_id)
        self.tokenizer_obj = tokenizer_obj
        
        if not isinstance(self.tokenizer_obj, Tokenizer):
            print("[TokenCompressor] - ERROR - The passed @param tokenizer_obj is not a instance of \"Tokenizer\"")
            exit(1)

    def output_tokens(self):
        """ Outputs the, now, compressed tokens
        in a more readable format if the compressed 
        tokens != 0 in length. """
        pass

    def compress(self):
        """ Main functionality in this function,
        compresses all whitelisted tokens (@member whitelist)
        for syntax-checking post-compression // lexing-tree. """
        pass # TODO => Finish compression with RegEx