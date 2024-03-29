'''Stats System
class stats:
	
	all_time_runs = 0

	def increment_all_time_runs(self):
		self.all_time_runs += 1			

	def show_all_time_runs(self):
		return self.all_time_runs

	def reset_all_time_runs(self):
		self.all_time_runs = 0

st = stats()

@client.command()
async def stats(ctx):
	embed = discord.Embed(title = "🦆 Duck4u Stats", description = "Here are all the available statistics: ", color = discord.Colour.blue())
	embed.add_field(name = "Daily", value = "Not Implemented yet", inline = True)
	embed.add_field(name = "Weekly", value = "Not Implemented yet", inline = True)
	embed.add_field(name = "Monthly", value = "Not Implemented yet", inline = True)
	
	embed.add_field(name = "All Time", value = f"{st.show_all_time_runs()}", inline = True)

	embed.set_footer(text=f"{ctx.author.display_name} is a noob.")

	await ctx.send(embed=embed)
	print(f"SUCCCESS : {dt.now(pytz.timezone('Asia/Kolkata'))} : stats shown")

# Place below in command method to increment counters
st.increment_all_time_runs()
'''