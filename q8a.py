import numpy as nmp
import matplotlib.pyplot as mtplt

def estimate_coeff(p, q):
    # Estimate the total number of points or observations
    n1 = nmp.size(p)

    # Calculate the mean of p and q vectors
    m_p = nmp.mean(p)
    m_q = nmp.mean(q)

    # Calculate the cross-deviation and deviation about p
    SS_pq = nmp.sum(q * p) - n1 * m_q * m_p
    SS_pp = nmp.sum(p * p) - n1 * m_p * m_p

    # Calculate the regression coefficients
    b_1 = SS_pq / SS_pp
    b_0 = m_q - b_1 * m_p

    return (b_0, b_1)

def plot_regression_line(p, q, b):
    # Plot the actual points or observations as a scatter plot
    mtplt.scatter(p, q, color="m", marker="o", s=30)

    # Calculate the predicted response vector
    q_pred = b[0] + b[1] * p

    # Plot the regression line
    mtplt.plot(p, q_pred, color="g")

    # Put the labels
    mtplt.xlabel('p')
    mtplt.ylabel('q')

    # Define the function to show the plot
    mtplt.show()

def main():
    # Enter the observation points or data
    p = nmp.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    q = nmp.array([11, 13, 12, 15, 17, 18, 18, 19, 20, 22])

    # Estimate the coefficients
    b = estimate_coeff(p, q)
    print("Estimated coefficients are:\\nb_0 = {}\\nb_1 = {}".format(b[0], b[1]))

    # Plot the regression line
    plot_regression_line(p, q, b)

if __name__ == "__main__":
    main()