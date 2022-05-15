from LinkedList import LinkedList
from Node import Node


def main():
  input_file_lines = open("input.txt","r").read().splitlines()
  output_file = open("output.txt","w")

  linked_list = LinkedList()

  for line in input_file_lines:
    words = line.split(' ')
    operation = words[0]
    value = int(words[1])

    if (operation == 'INC'):
      linked_list.append(value)

    if (operation == 'REM'):
      linked_list.remove(value)

    if (operation == 'SUC'):
      # TODO
      pass

    if (operation == 'IMP'):
      for node in linked_list:
        output_file.write(node.value + " ")

      pass
    
    print(linked_list)

main()