import command_parser
import sys

if __name__ == '__main__':
    media_type, time_window, output_format = sys.argv[1], sys.argv[2], sys.argv[3]

    command_parser.parse(media_type, time_window, output_format)
    # command_parser.parse('all', 'day', 'json')