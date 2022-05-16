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
      print(linked_list)
      print(f'{str(value)} inserted')
      print(" ")

    if (operation == 'REM'):
      linked_list.remove(value)
      print(linked_list)
      print(f'{str(value)} removed')
      print(" ")

    if (operation == 'SUC'):
      output_file.write(words[0] + " " + words[1] + " " + words[2] + "\n")

      successor = linked_list.successor(int(words[1]), int(words[2]))
      
      if successor is None:
        successor = "INF"

      output_file.write(str(successor) + "\n")
      pass

    if (operation == 'IMP'):
      versioned_list = linked_list.get_list_by_version(value)

      output_file.write(words[0] + " " + words[1] + "\n")
      for node in versioned_list:
        output_file.write(str(node) + " ")
      output_file.write("\n")
      pass

main()