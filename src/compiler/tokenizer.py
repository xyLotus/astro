""" The file where the definition of the Tokenizer
class is stored. """

from astro_file import AstroFile
from astro_types import Token


class Tokenizer:
    """ This class tokenizes the given files
    given in @member h_file and returns the tokens
    per line uncompressed and raw. """
    
    def __init__(self, h_file: AstroFile):
        """ @member file = file to be tokenized,
        @member tokens, token list; used in @method tokenize. """
        self.h_file = h_file
        self.tokens = []

        with open(h_file.file_name, 'r') as f:
            self.content = f.read()

        self._preset_tokens = [
            'TOK_SYM',      # ANY Symbol
            'TOK_SPACE',    # ' '
            'TOK_FUNCINIT', # !
            'TOK_COMMA',    # ,
            'TOK_COLON',     # :
            'TOK_LFBRACKET',
            'TOK_RGBRACKET'
        ]

    def output_tokens(self):
        """ debug outputs tokens for better readability
        accesses @member tokens, returns error if list is empty. """
        if len(self.tokens) == 1 and len(self.tokens[0]) == 0:
            print('[TOKENIZER] - ERROR - @member self.tokens is empty.')
            exit(1)

        for line in self.tokens:
            for token in line:
                if   token.token_id == 1: print('[TOK_SPACE]',     end=' ')
                elif token.token_id == 2: print('[TOK_FUNCINIT]',  end=' ')
                elif token.token_id == 3: print('[TOK_COMMA]',     end=' ')
                elif token.token_id == 4: print('[TOK_COLON]',     end=' ')
                elif token.token_id == 5: print('[TOK_LFBRACKET]', end=' ')
                elif token.token_id == 6: print('[TOK_RGBRACKET]', end=' ')
                else:                     print('[TOK_SYM]',       end=' ')
            print()

    def _construct_token(self, tok_id: int, tok_value: str):
        tok = Token()
        tok.token_id    = tok_id
        tok.token_value = tok_value

        return tok

    def tokenize(self):
        """ Main method for tokenizing,
        parses file with file handle @member h_file. """
        # stores a new line of iteratively generated tokens
        # each iteration, used for appending @member tokens
        tokl_buf = []

        # Iteratively assigning TokenIDs to file content
        # for each line, used for appending @var tokl_buf
        for line in self.content.split('\n'):
            for c in line:
                if c == ' ':
                    tokl_buf.append(self._construct_token(1, c))
                elif c == '!':
                    tokl_buf.append(self._construct_token(2, c))
                elif c == ',':
                    tokl_buf.append(self._construct_token(3, c))
                elif c == ':':
                    tokl_buf.append(self._construct_token(4, c))
                elif c == '(':
                    tokl_buf.append(self._construct_token(5, c))
                elif c == ')':
                    tokl_buf.append(self._construct_token(6, c))
                else:
                    tokl_buf.append(self._construct_token(0, c))
            
            self.tokens.append(tokl_buf)
            tokl_buf = [] # reset buffer
                
