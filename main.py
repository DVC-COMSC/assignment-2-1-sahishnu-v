def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    m_num = int(input('Number of male students? '))
    f_num = int(input('Number of female students? '))
    total = m_num + f_num
    m_perc = m_num / total * 100
    f_perc = f_num / total * 100
    
    print(f'The total number of students: {total} ')
    print(f'The number of males and females: {m_num}  {f_num} ')
    print(f'The percentage of males and females: {m_perc:.2f}%  {f_perc:.2f}% ')
    return m_perc, f_perc


if __name__ == '__main__':
    main()
