import taipy as tp
import my_config

if __name__ == "__main__":
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)
    sequence = scenario.sales_sequence

    sequence_retrieved = tp.get(sequence.id)