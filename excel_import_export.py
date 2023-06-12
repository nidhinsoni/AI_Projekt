#EXCEL EXPORT
    def input_values(file_path, sheet_name, row, column, values):
        # Load the workbook
        workbook = openpyxl.load_workbook(file_path)
        # Select the sheet
        sheet = workbook[sheet_name]
        # Input values at the specified row/column
        for i, value in enumerate(values):
            sheet.cell(row=row, column=column + i).value = value
        # Save the workbook
        workbook.save(file_path)
        # Close the workbook
        workbook.close()

    # Example usage
    file_path = 'D:\EIT Studium\AI Projekt\Excel\Dataset_test.xlsx'
    sheet_name = 'Sheet1'
    row = 3
    column = 1
    values = ['Value1', 'Value2', 'Value3']

    input_values(file_path, sheet_name, row, column, values)