import csv


def getPlayerData(csv_filename):
    """Returns the stats of all the players in the specified csv file

    Args:
        csv_filename (.csv): [csv file that contains the stats of all the players]

    Returns:
        [fields, rows]: [stat names, stats]
    """
    fields = []
    rows = []

    with open(csv_filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        fields = next(csv_reader)
        for row in csv_reader:
            rows.append(row)
    return fields, rows
