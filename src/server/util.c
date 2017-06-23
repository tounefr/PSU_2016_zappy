
char is_legal_network_char(char c)
{
    return (!(c >= 32 && c <= 126) &&
            c != '\n');
}