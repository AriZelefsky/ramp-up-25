def ave_spd(up_time, up_spd, down_spd):
	larger = up_spd if up_spd > down_spd else down_spd
	smaller = up_spd if up_spd < down_spd else down_spd

	times = larger / smaller

	return (larger + (times)*(smaller)) / (times +1)