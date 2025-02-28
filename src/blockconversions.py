from textnode import TextNode, TextType

def markdown_to_blocks(text: str):
    # Split into blocks and filter out empty ones
    list_of_blocks = [block.strip() for block in text.split('\n\n') if block.strip()]
    
    # Process each block to handle multi-line indentation
    processed_blocks = []
    for block in list_of_blocks:
        # Split block into lines, strip each line, and rejoin
        lines = block.split('\n')
        dedented_block = '\n'.join([line.strip() for line in lines])
        processed_blocks.append(dedented_block)
    
    # Process each block to handle indentation with a list comprehension, alternate option for my notes.
    # return ['\n'.join([line.strip() for line in block.split('\n')]) for block in list_of_blocks]

    return processed_blocks