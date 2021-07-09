""" The main file is the entrypoint for execution of astro,
the where all the dev intended execution order takes places. """

from astro_file import AstroFile
from tokenizer import Tokenizer
from token_compressor import TokenCompressor


# seperator
print()

TOK_SYM     = 0
TOK_SPACE   = 1
TOK_FUNCINI = 2
TOK_COMMA   = 3
TOK_COLON   = 4



file_handle = AstroFile(
    file_name = "astro_code.txt", 
    cleanup = False
)

tokenizer = Tokenizer(
    h_file = file_handle
)
tokenizer.tokenize()
tokenizer.output_tokens()


token_compressor = TokenCompressor(
     tokenizer_obj = tokenizer,
     compress_id = TOK_SYM
)

# seperator
print()
