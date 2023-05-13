
#2d list called 'grid' which will be used in the code:
grid = [
    ["-" , "-", "-", "#", "-"],
    ["-" , "#", "-", "-", "#"],
    ["#" , "-", "-", "-", "-"],
    ["-" , "-", "#", "-", "-"],
    ["-" , "-", "-", "-", "#"]
]

# rough copy of intended output at the end of the code. #grid easier to type than minesweeper....
'''minesweeper = [
    ["1" , "1", "2", "#", "2"],
    ["2" , "#", "2", "2", "#"],
    ["#" , "3", "1", "2", "1"],
    ["1" , "2", "#", "2", "1"],
    ["0" , "1", "1", "2", "#"]
]'''

#'enumerate' function iterates over rows and items and creates new variables
for row_index, row in enumerate(grid): #outer 'for' loop; variables 'row_index' (index of current row) and 'row' (items in row) created
    for col_index, item in enumerate(row): #inner/nested 'for' loop ; variables 'col_index' (for items in row) and 'item' (the item, i.e. # or -)
        if item == '#':
            continue  #skips counting bombs for cells that already contain a bomb as these items do not need a numerical value

        #calculating number of bombs in adjacent positions
        bomb_count = 0 #variable created to help populate cells with numbers of adjacent bombs
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue  # skip current cell
                adj_row = row_index + i #adj_row and adj_col variables ('adj' as couldn't be bothered to keep typing adjacent...)
                adj_col = col_index + j #both variables are to represent indices of adjacent cells around the one being iterated over.
                if adj_row < 0 or adj_row >= len(grid):
                    continue  # this skips adjacent cells outside of grid boundaries preventing 'out of range' error
                if adj_col < 0 or adj_col >= len(row):
                    continue  # skip adjacent cells outside of grid boundaries as with rows
                if grid[adj_row][adj_col] == '#':
                    bomb_count += 1 #increments bomb_count by 1 for each "#" in adjacent cell
        grid[row_index][col_index] = bomb_count #refers back to 2d list using above block of code replacing '-' with number of adjacent bombs.


#displays completed minesweeper board with each value on its row separated by spaces
for row in grid:
    for item in row:
        print(item, end=' ')
    print()