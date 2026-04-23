def proverb(*args: str, qualifier: str = "") -> list[str]:
    
    keywords = list(args)
    
    output = []
    
    try:
        nail = keywords[0]
    except IndexError:
        pass
    else:
        if len(keywords) > 1:
            output = [f'For want of a {keywords[idx]} the {keywords[idx + 1]} was lost.'
                  for idx in range(0, len(keywords) - 1)]
        
        final_line = "And all for the want of a "
        
        if qualifier:
            final_line += f'{qualifier} {nail}.'
        else:
            final_line += f'{nail}.'
        
        output.append(final_line)
    
    return output
