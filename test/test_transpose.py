import pandas as pd

# Create the original table
data = {
    'USA': ['', 'run', 'move', 'start', '', 'sleep'],
    'China': ['walk', '', '', '', 'go', '']
}
df = pd.DataFrame(data, index=['Round 1', 'Round 2', 'Round 3', 'Round 4', 'Round 5', 'Round 6'])
print('Original table:\n', df)

# Melt the table into a new format
melted_df = df.reset_index().melt(id_vars='index', var_name='team', value_name='action')
melted_df.columns = ['round', 'team', 'action']
melted_df = melted_df[melted_df['action'] != ''] # Remove rows with empty action

print('\nNew table:\n', melted_df)