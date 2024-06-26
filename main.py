def main():
    ##################################################
    # Comlete your code here
    ##################################################
    """
    Use following variables to save your result
    total 
    average
    """
    # Input three values
    val1 = int(input())
    val2 = int(input())
    val3 = int(input())

    # Calculate the total
    total = val1 + val2 + val3

    #Calulate the average
    average = total / 3

    # Print the Values, Total, and Average
    print (f'Values: {val1} {val2} {val3}')
    print (f'Total: {total}')
    print (f'Average: {average:.2f}')

    ########################################
    # Do not delete the return statement
    ########################################
    return total, average


if __name__ == '__main__':
    main()
