# Table2Graph

Generate graphs/charts from tables (CSVs)

Input: 
Not Finalised yet, Will get Input as form-data as in postman.  

Output_JSON: 
```bazaar
[
    {
        analysis_type: "bivariant_analysis",
        analysis_name: "Bivariant Analysis",
        data: [
            {
                chart_type: 'bar_chart',
                chart_data: [
                    {
                        title: 'Age vs Survival',
                        label: {
                            x: 'Age',
                            y: 'Survival'
                        },
                        values: {
                            x: [0, 1],
                            y: [10, 20]
                        },
                        legends: {
                            0: 'Age',
                            1: 'Survival'
                        }
                    }
                ]
            }
        ]
    },
    {
        analysis_type: "univariant_analysis",
        analysis_name: "univariant Analysis",
        data: [
            {
                chart_type: 'bar_chart',
                chart_data: [
                    {
                        title: 'Age vs Survival',
                        label: {
                            x: 'Age',
                            y: 'Survival'
                        },
                        values: {
                            x: [0, 1],
                            y: [10, 20]
                        },
                        legends: {
                            0: 'Age',
                            1: 'Survival'
                        }
                    }
                ]
            }
        ]
    }
]
```