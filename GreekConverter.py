from GUI_Module import GUI

def convert_to_greek(text):
    conversion_dict = {
    'a': 'α', 'A': 'Δ',
    'b': 'β', 'B': 'Β',
    'c': 'c', 'C': 'C',
    'd': 'δ', 'D': 'D',
    'e': 'ε', 'E': 'Ε',
    'f': 'f', 'F': 'Γ',
    'g': 'φ', 'G': 'Φ',
    'h': 'h', 'H': 'Η',
    'i': 'ι', 'I': 'Ι',
    'j': 'ϕ', 'J': 'ϕ',
    'k': 'κ', 'K': 'Κ',
    'l': 'λ', 'L': 'Λ',
    'm': 'μ', 'M': 'Μ',
    'n': 'n', 'N': 'Π',
    'o': 'ο', 'O': 'Ο',
    'p': 'ρ', 'P': 'Ρ',
    'q': 'Ω', 'Q': 'Ώ',
    'r': 'r', 'R': 'Γ',
    's': 's', 'S': 'S',
    't': 'τ', 'T': 'Τ',
    'u': 'υ', 'U': 'U',
    'v': 'ω', 'V': 'V',
    'w': 'ώ', 'W': 'W',
    'x': 'χ', 'X': 'Χ',
    'y': 'γ', 'Y': 'λ',
    'z': 'ζ', 'Z': 'Ζ'
}


    converted_text = ''.join(conversion_dict[char] if char in conversion_dict else char for char in text)

    return converted_text

GUI(convert_to_greek)